from PyQt5.QtWidgets import QSlider

def reset_sliders(self):
    for slider in [
        self.verticalSlider_6,
        self.verticalSlider_9,
        self.verticalSlider_8,
        self.verticalSlider_7,
        self.verticalSlider_5,
        self.verticalSlider,
        self.verticalSlider_2,
        self.verticalSlider_3,
        self.verticalSlider_4,
    ]:
        slider.setValue(50)