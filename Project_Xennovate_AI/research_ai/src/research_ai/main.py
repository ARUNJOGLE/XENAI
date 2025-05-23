#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import ResearchAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

user_input = input("Enter a topic: ")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': user_input,
        'current_year': str(datetime.now().year)
    }
    
    try:
        ResearchAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()