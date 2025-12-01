"""
Example: How to use the workflow orchestrator with your own API integration.

This shows the pattern without revealing specific API implementations.
"""
from pathlib import Path
from scripts.workflow_orchestrator import orchestrate_workflow
from scripts.prompt_parser import SceneData


def example_image_generator(scene: SceneData, output_dir: Path):
    """
    Example image generation function.
    
    Replace this with your own API integration (fal.ai, DALL-E, Midjourney, etc.)
    
    Args:
        scene: Scene data from parsed script
        output_dir: Directory to save output
    """
    # Example structure - replace with your API
    print(f"  Generating image for scene {scene.scene_number}...")
    
    # Your API call would go here:
    # result = your_api.generate_image(
    #     prompt=scene.initial_prompt,
    #     size=(1080, 1920)
    # )
    # 
    # download_image(result['url'], output_dir / "final.png")
    
    print(f"  (Replace with your actual API integration)")


def example_audio_generator(scene: SceneData, output_dir: Path):
    """
    Example audio generation function.
    
    Replace this with your own API integration (ElevenLabs, Azure TTS, etc.)
    
    Args:
        scene: Scene data from parsed script
        output_dir: Directory to save output
    """
    from scripts.narration_extractor import get_narration_for_scene
    
    # Extract narration
    narration = get_narration_for_scene(
        Path("examples/sample_explainer.txt"),
        scene.scene_number
    )
    
    print(f"  Generating audio for scene {scene.scene_number}...")
    
    # Your API call would go here:
    # result = your_api.generate_audio(
    #     text=narration,
    #     voice_id="your-voice-id"
    # )
    # 
    # save_audio(result, output_dir / "narration.mp3")
    
    print(f"  (Replace with your actual API integration)")


def main():
    """Example usage"""
    explainer_path = Path("examples/sample_explainer.txt")
    
    # Example 1: Image generation workflow
    print("=" * 70)
    print("EXAMPLE 1: Image Generation Workflow")
    print("=" * 70)
    
    stats = orchestrate_workflow(
        explainer_path=explainer_path,
        process_scene=example_image_generator,
        output_filename="final.png"
    )
    
    print(f"\nStats: {stats}")
    
    # Example 2: Audio generation workflow
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Audio Generation Workflow")
    print("=" * 70)
    
    stats = orchestrate_workflow(
        explainer_path=explainer_path,
        process_scene=example_audio_generator,
        output_filename="narration.mp3"
    )
    
    print(f"\nStats: {stats}")


if __name__ == "__main__":
    main()

