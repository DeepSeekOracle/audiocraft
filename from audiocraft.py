from audiocraft.models import MusicGen

model = MusicGen.get_pretrained("facebook/musicgen-stereo-medium")

descriptions = ['happy rock', 'energetic EDM', 'sad jazz']
wav = model.generate(descriptions)  # generates 3 samples.