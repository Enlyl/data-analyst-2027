import json
import os

def create_notebook(filepath, cells):
    """
    Создает валидный Jupyter Notebook (.ipynb) v4
    cells: список кортежей ("markdown" | "code", source_str)
    """
    nb_cells = []
    for cell_type, src in cells:
        # lines split
        lines = [line + "\n" for line in src.split("\n")]
        if lines:
            lines[-1] = lines[-1].rstrip("\n")
            
        if cell_type == "markdown":
            nb_cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": lines
            })
        elif cell_type == "code":
            nb_cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": lines
            })
            
    notebook_structure = {
        "cells": nb_cells,
        "metadata": {
            "colab": {
                "provenance": []
            },
            "kernelspec": {
                "display_name": "Python 3",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 0
    }
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(notebook_structure, f, ensure_ascii=False, indent=2)
    print(f"Created notebook: {filepath}")
