import streamlit as st
import pandas as pd
import joblib
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor  # ใช้สำหรับ Neural Network Model
from pathlib import Path

def display_ml_model():
    
    base_path = Path(__file__).parent.parent / "ML"