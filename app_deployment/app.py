from fastai.vision.all import *
import gradio as gr
from pathlib import Path

#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

nut_labels = (
    "raw Almonds",
    "raw Walnuts",
    "raw Cashew nut",
    "raw Pecans",
    "raw Peanut",
    "raw Pili nut",
    "raw Pistachios nut",
    "raw Hazelnuts",
    "raw Brazil nut",
    "raw Maccademia nut",
    "raw Pine nut",
    "raw Chestnut",
    "raw Hickory nut",
    "raw Ginkgo nut"
)

model = load_learner('nut-recognizer-v4 .pkl')


def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(nut_labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'Pistachio.jpg',
    'cashew.jpg',
    'macadamia-nut.jpg',
    'peanuts.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)
