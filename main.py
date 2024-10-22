from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Project(BaseModel):
    id: int
    title: str
    description: str
    image_url: str
    project_url: str


# Sample data
projects = [
    Project(
        id=1,
        title="AI-Powered Chatbot",
        description="Developed an intelligent chatbot using natural language processing to enhance customer support.",
        image_url="https://images.unsplash.com/photo-1660592868727-858d28c3ba52?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fHByb2plY3R8ZW58MHx8MHx8fDA%3D",
        project_url="https://example.com/chatbot"
    ),
    Project(
        id=2,
        title="Machine Learning Recommendation System",
        description="Built a recommendation engine using collaborative filtering to personalize user experiences.",
        image_url="https://images.unsplash.com/photo-1685478237284-1a791984c17a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzZ8fHByb2plY3R8ZW58MHx8MHx8fDA%3D",
        project_url="https://example.com/recommendation"
    ),
    Project(
        id=3,
        title="Computer Vision Object Detection",
        description="Implemented a real-time object detection system using deep learning and computer vision techniques.",
        image_url="https://images.unsplash.com/photo-1634937809683-ddb52aa8ec62?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fHByb2plY3R8ZW58MHx8MHx8fDA%3D",
        project_url="https://example.com/object-detection"
    ),
    Project(
        id=4,
        title="Predictive Maintenance System",
        description="Developed a predictive maintenance solution using IoT sensors and machine learning algorithms.",
        image_url="https://images.unsplash.com/photo-1666321793574-aa14eb7e159c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDZ8fHByb2plY3R8ZW58MHx8MHx8fDA%3D",
        project_url="https://example.com/predictive-maintenance"
    ),
    Project(
        id=5,
        title="Natural Language Processing for Sentiment Analysis",
        description="Created a sentiment analysis tool to analyze customer feedback and social media mentions.",
        image_url="https://images.unsplash.com/photo-1492551557933-34265f7af79e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTJ8fHByb2plY3R8ZW58MHx8MHx8fDA%3D",
        project_url="https://example.com/sentiment-analysis"
    )
]


@app.get("/projects", response_model=List[Project])
async def get_projects():
    return projects
