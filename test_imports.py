#!/usr/bin/env python3
"""Test script to verify all imports work correctly"""

print("Testing imports...")

try:
    print("✓ Testing Flask...")
    from flask import Flask
    
    print("✓ Testing src.helper...")
    from src.helper import download_hugging_face_embeddings
    
    print("✓ Testing langchain_pinecone...")
    from langchain_pinecone import PineconeVectorStore
    
    print("✓ Testing langchain_openai...")
    from langchain_openai import ChatOpenAI
    
    print("✓ Testing langchain_classic chains...")
    from langchain_classic.chains import create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    
    print("✓ Testing langchain_core...")
    from langchain_core.prompts import ChatPromptTemplate
    
    print("✓ Testing dotenv...")
    from dotenv import load_dotenv
    
    print("\n✅ All imports successful!")
    print("\nNow testing app initialization...")
    
    # Test basic app setup
    app = Flask(__name__)
    load_dotenv()
    
    print("✅ App initialization successful!")
    print("\nYour Medical Chatbot is ready to run!")
    print("Run: python app.py")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
