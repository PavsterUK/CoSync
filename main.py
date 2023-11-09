from flask import Flask
from app.audio_transcription import transcription_blueprint
from app.diarization import diarization_blueprint
from app.text_analysis import analysis_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

app.register_blueprint(transcription_blueprint)
app.register_blueprint(diarization_blueprint)
app.register_blueprint(analysis_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
