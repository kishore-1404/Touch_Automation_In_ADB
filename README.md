# Touch Automation and Text Extraction

## Overview

This project automates touch events on an Android device and extracts text from specific screen regions. It uses `uiautomator2` for device interaction, `Pillow` for image processing, `easyocr` for optical character recognition, and `pytesseract` as an alternative OCR solution. This README provides an overview of each script's functionality and how to use them.

## Prerequisites

- Python 3.x installed
- Required Python packages:
  - `uiautomator2`
  - `Pillow`
  - `easyocr`
  - `numpy`
  - `pytesseract`
- An Android device or emulator with ADB enabled

## Installation

1. Install the necessary Python packages:

   ```bash
   pip install uiautomator2 Pillow easyocr numpy pytesseract
