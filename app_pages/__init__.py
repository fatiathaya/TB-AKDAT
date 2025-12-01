"""
Page components for ForestCal application
"""

from .home_page import render_home_page
from .dataset_page import render_dataset_page
from .preprocessing_page import render_preprocessing_page
from .training_page import render_training_page
from .visualization_page import render_visualization_page
from .analysis_page import render_analysis_page

__all__ = [
    'render_home_page',
    'render_dataset_page',
    'render_preprocessing_page',
    'render_training_page',
    'render_visualization_page',
    'render_analysis_page'
]

