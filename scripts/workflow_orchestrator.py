"""
Generic workflow orchestrator pattern for batch processing explainer scenes.

This module provides a reusable pattern for orchestrating workflows without
including specific API integrations. Users can plug in their own processing functions.

Example:
    def my_image_generator(scene):
        # Your API integration here
        result = your_api.generate_image(scene.initial_prompt)
        save_image(result, output_path)
    
    orchestrate_workflow(
        explainer_path=Path("examples/sample.txt"),
        process_scene=my_image_generator
    )
"""
import time
import sys
from pathlib import Path
from typing import Callable, List, Optional, Dict, Any

# Handle imports for both package and direct execution
try:
    from scripts.prompt_parser import parse_explainer_file, SceneData, get_scene_output_dir
except ImportError:
    # Fallback for direct execution
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from scripts.prompt_parser import parse_explainer_file, SceneData, get_scene_output_dir


def check_output_exists(output_dir: Path, filename: str = "final.png") -> bool:
    """
    Check if output already exists for a scene.
    
    Args:
        output_dir: Directory where output would be saved
        filename: Name of the output file to check
        
    Returns:
        True if file exists, False otherwise
    """
    return (output_dir / filename).exists()


def filter_scenes(
    scenes: List[SceneData],
    scene_numbers: Optional[List[int]] = None
) -> List[SceneData]:
    """
    Filter scenes by scene numbers.
    
    Args:
        scenes: List of all scenes
        scene_numbers: Optional list of scene numbers to include
        
    Returns:
        Filtered list of scenes
    """
    if scene_numbers is None:
        return scenes
    return [s for s in scenes if s.scene_number in scene_numbers]


def handle_error(scene: SceneData, error: Exception, continue_on_error: bool = True) -> bool:
    """
    Handle errors during scene processing.
    
    Args:
        scene: The scene that failed
        error: The exception that occurred
        continue_on_error: Whether to continue processing other scenes
        
    Returns:
        True if should continue, False if should stop
    """
    print(f"\n❌ Error processing Scene {scene.scene_number}: {error}")
    
    if continue_on_error:
        response = input("Continue with remaining scenes? (y/n): ")
        return response.lower() == 'y'
    
    return False


def orchestrate_workflow(
    explainer_path: Path,
    process_scene: Callable[[SceneData, Path], Any],
    scene_numbers: Optional[List[int]] = None,
    skip_existing: bool = True,
    output_base_dir: Path = None,
    output_filename: str = "final.png",
    continue_on_error: bool = True
) -> Dict[str, Any]:
    """
    Generic workflow orchestrator for batch processing scenes.
    
    This function provides the orchestration pattern (batching, progress tracking,
    error handling) while allowing users to plug in their own processing functions.
    
    Args:
        explainer_path: Path to explainer .txt file
        process_scene: User-provided function to process each scene
                      Signature: process_scene(scene: SceneData, output_dir: Path) -> Any
        scene_numbers: Optional list of specific scene numbers to process
        skip_existing: If True, skip scenes that already have output
        output_base_dir: Base directory for output (default: "output")
        output_filename: Filename to check for existing output
        continue_on_error: Whether to continue processing after errors
        
    Returns:
        Dict with statistics: {
            'total': int,
            'completed': int,
            'skipped': int,
            'failed': int,
            'elapsed_time': float
        }
    
    Example:
        def my_image_generator(scene, output_dir):
            # Your API integration
            image = your_api.generate(scene.initial_prompt)
            save_image(image, output_dir / "final.png")
        
        stats = orchestrate_workflow(
            explainer_path=Path("examples/sample.txt"),
            process_scene=my_image_generator
        )
    """
    if not explainer_path.exists():
        raise FileNotFoundError(f"Explainer file not found: {explainer_path}")
    
    if output_base_dir is None:
        output_base_dir = Path("output")
    
    # Parse the explainer file
    data = parse_explainer_file(explainer_path)
    explainer_name = explainer_path.stem
    
    print(f"\n{'='*70}")
    print(f"WORKFLOW ORCHESTRATION: {explainer_path.name}")
    print(f"{'='*70}\n")
    print(f"Title: {data['title']}")
    print(f"Total Duration: {data['total_duration']} seconds")
    print(f"Format: {data['format']}")
    print(f"Total Scenes: {len(data['scenes'])}")
    
    # Filter scenes
    scenes = filter_scenes(data['scenes'], scene_numbers)
    
    if scene_numbers:
        print(f"Processing scenes: {scene_numbers}")
    else:
        print(f"Processing all scenes")
    
    if not scenes:
        print("No scenes to process!")
        return {
            'total': 0,
            'completed': 0,
            'skipped': 0,
            'failed': 0,
            'elapsed_time': 0.0
        }
    
    print()
    
    # Track statistics
    total = len(scenes)
    completed = 0
    skipped = 0
    failed = 0
    
    start_time = time.time()
    
    # Process each scene
    for i, scene in enumerate(scenes, 1):
        output_dir = get_scene_output_dir(output_base_dir, explainer_name, scene.scene_number)
        
        # Check if already exists
        if skip_existing and check_output_exists(output_dir, output_filename):
            print(f"\n[{i}/{total}] Scene {scene.scene_number}: {scene.title}")
            print(f"  ⏭️  Skipping (output already exists)")
            skipped += 1
            continue
        
        try:
            print(f"\n[{i}/{total}] Processing Scene {scene.scene_number}: {scene.title}")
            process_scene(scene, output_dir)
            completed += 1
            print(f"  ✅ Completed")
            
        except Exception as e:
            print(f"  ❌ Failed")
            failed += 1
            
            if not handle_error(scene, e, continue_on_error):
                break
    
    # Calculate elapsed time
    elapsed = time.time() - start_time
    elapsed_min = int(elapsed // 60)
    elapsed_sec = int(elapsed % 60)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"WORKFLOW COMPLETE")
    print(f"{'='*70}")
    print(f"Total scenes: {total}")
    print(f"✅ Completed: {completed}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"❌ Failed: {failed}")
    print(f"⏱️  Time: {elapsed_min}m {elapsed_sec}s")
    print(f"\nOutput directory: {output_base_dir / explainer_name}")
    print(f"{'='*70}\n")
    
    return {
        'total': total,
        'completed': completed,
        'skipped': skipped,
        'failed': failed,
        'elapsed_time': elapsed
    }


def main():
    """Example usage - shows how to use the orchestrator"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Workflow orchestrator example',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This is a generic orchestrator. You need to provide your own processing function.

Example implementation:
    def my_processor(scene, output_dir):
        # Your API integration here
        result = your_api.process(scene)
        save_result(result, output_dir)
    
    orchestrate_workflow(
        explainer_path=Path("examples/sample.txt"),
        process_scene=my_processor
    )
        """
    )
    
    parser.add_argument(
        'explainer_file',
        type=Path,
        help='Path to explainer .txt file'
    )
    
    parser.add_argument(
        '--scenes',
        type=int,
        nargs='+',
        help='Specific scene numbers to process (default: all)'
    )
    
    parser.add_argument(
        '--no-skip',
        action='store_true',
        help='Process even if output already exists'
    )
    
    args = parser.parse_args()
    
    # Example: Dummy processor (users replace with their own)
    def dummy_processor(scene: SceneData, output_dir: Path):
        """Dummy processor - replace with your own implementation"""
        print(f"  Processing scene {scene.scene_number}...")
        print(f"  (Replace this with your own processing function)")
        # output_dir.mkdir(parents=True, exist_ok=True)
        # Your processing logic here
    
    orchestrate_workflow(
        explainer_path=args.explainer_file,
        process_scene=dummy_processor,
        scene_numbers=args.scenes,
        skip_existing=not args.no_skip
    )


if __name__ == "__main__":
    main()

