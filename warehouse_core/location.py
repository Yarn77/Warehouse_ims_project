from abc import ABC, abstractmethod
import os

# =====================================================================
# [OOP CONCEPT 1: COMPOSITION ('HAS-A' RELATIONSHIP)]
# Location represents physical warehouse positioning. BaseProduct HAS-A Location.
# Decouples spatial layout tracking from pricing and stock rules.
# =====================================================================
class Location:
    def __init__(self, rack: str):
        self.rack = rack

# 