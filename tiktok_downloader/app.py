from flask import Flask, render_template, request, jsonify, send_file
import requests
import os
app = Flask(__name__)
def download_tiktok_video(url):
    api = "https://www.tikwm.com/api/"
    params = {"url": url}
    response = requests.get(api, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("data"):
            return data["data"]["play"]
    return None
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/download', methods=['POST'])
def download():
    tiktok_url = request.json.get('url')
    if not tiktok_url:
        return jsonify({"error": "សូម​បញ្ចូល​ ​URL​ ឬ Link"}), 400
    video_link = download_tiktok_video(tiktok_url)
    if video_link:
        return jsonify({"success": True, "video": video_link})
    else:
        return jsonify({"success": False, "error": "មិន​អាច​ទៅ​យក​វីដេអូទេ"})
@app.route('/download_file')
def download_file():
    video_url = request.args.get('video_url')
    if not video_url:
        return "មិនបានផ្តល់ URL វីដេអូទេ", 400
    try:
        r = requests.get(video_url)
        filename = "tiktok_video.mp4"
        filepath = os.path.join(os.getcwd(), filename)

        with open(filepath, "wb") as f:
            f.write(r.content)

        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return f"Error downloading file: {e}", 500
    finally:
        pass
if __name__ == '__main__':
    app.run(debug=True)