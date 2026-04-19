# PicoLevel-Visualizer 🚥

An analog level monitoring system built with Raspberry Pi Pico.

## 🚀 Overview
This project reads an analog value (0-65535) from a potentiometer and converts it into a visual scale using a 10-segment LED bar. When the level reaches its maximum, a buzzer is activated as an audible alert.

## 🛠️ Components
* **Microcontroller:** Raspberry Pi Pico W
* **Visual Output:** 10-segment LED Bar (or 10 individual LEDs)
* **Resistors:** 10x 220Ω (for LED protection)
* **Input:** 1x Potentiometer
* **Audio Alert:** 1x Active/Passive Buzzer
* **Other:** Breadboard and jumper wires

## 🔌 Wiring Diagram Logic
* **LEDs:** Connected to pins **GP6** through **GP15**.
* **Potentiometer:** Middle pin connected to **GP26 (ADC0)**.
* **Buzzer:** Connected to **GP16** (or your chosen digital pin).

## 💻 How to use
1. Clone this repository or copy the `main.py` file.
2. Flash the [MicroPython firmware](https://micropython.org/download/RPI_PICO/) onto your Raspberry Pi Pico.
3. Use **Thonny IDE** or any other compatible editor to upload `main.py` to the board.
4. Rotate the potentiometer to see the LEDs light up and hear the buzzer at the maximum level.
