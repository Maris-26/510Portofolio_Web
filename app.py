from flask import Flask, render_template_string

app = Flask(__name__)

# 主题与本地图片数据
portfolio_groups = [
    {
        'key': 'sakura',
        'title': 'Sakura | 樱花',
        'images': [
            '/static/photos/Sakura-1.jpg',
            '/static/photos/Sakura-2.jpg',
        ]
    },
    {
        'key': 'muse',
        'title': 'Muse | 少女',
        'images': [
            '/static/photos/Muse-1.jpg',
            '/static/photos/Muse-2.jpg',
        ]
    },
    {
        'key': 'botanica',
        'title': 'Botanica | 植物园',
        'images': [
            '/static/photos/Botanica-1.jpg',
            '/static/photos/Botanica-2.jpg',
        ]
    },
    {
        'key': 'pier',
        'title': 'Pier | 码头',
        'images': [
            '/static/photos/Pier-1.jpg',
            '/static/photos/Pier-2.jpg',
        ]
    },
]

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haichao Xing | Photography Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;400&display=swap" rel="stylesheet">
    <style>
        body {
            background: #fff;
            color: #222;
            font-family: 'Montserrat', serif;
            margin: 0;
            min-height: 100vh;
        }
        .main {
            display: flex;
            min-height: 100vh;
        }
        .sidebar {
            width: 320px;
            background: #fff;
            padding: 36px 0 0 60px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .sidebar h1 {
            font-size: 1.6em;
            font-weight: 700;
            margin-bottom: 2.5em;
            letter-spacing: 0.03em;
            white-space: nowrap;
        }
        .sidebar .nav {
            display: flex;
            flex-direction: column;
            gap: 1.6em;
        }
        .sidebar .nav .nav-item {
            font-size: 1.18em;
            color: #222;
            cursor: pointer;
            opacity: 0.82;
            border-left: 3px solid transparent;
            padding-left: 0.5em;
            transition: color 0.18s, border-color 0.18s, opacity 0.18s;
            white-space: nowrap;
        }
        .sidebar .nav .nav-item.active {
            color: #000;
            font-weight: 700;
            border-left: 3px solid #111;
            opacity: 1;
        }
        .content {
            margin-left: 320px;
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: #fff;
        }
        .photo-block {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 80vw;
            max-width: 1000px;
            min-height: 60vh;
            background: none;
            box-shadow: none;
            border-radius: 0;
            overflow: visible;
        }
        .photo-block img {
            max-width: 100%;
            max-height: 80vh;
            width: auto;
            height: auto;
            object-fit: contain;
            cursor: pointer;
            border-radius: 8px;
            background: none;
            box-shadow: 0 2px 16px #0001;
            transition: opacity 0.2s;
        }
        @media (max-width: 900px) {
            .sidebar { width: 100vw; padding: 24px 0 0 18px; }
            .content { margin-left: 0; }
            .main { flex-direction: column; }
            .photo-block { width: 96vw; min-height: 220px; }
        }
    </style>
</head>
<body>
    <div class="main">
        <div class="sidebar">
            <h1>Haichao Xing</h1>
            <div class="nav">
                {% for group in groups %}
                <div class="nav-item{% if loop.first %} active{% endif %}" data-key="{{ group.key }}">{{ group.title }}</div>
                {% endfor %}
            </div>
        </div>
        <div class="content">
            <div class="photo-block" id="photo-block">
                <img id="theme-img" src="{{ groups[0].images[0] }}" alt="photo">
            </div>
        </div>
    </div>
    <script>
        const groups = {{ groups|tojson }};
        let currentGroup = 0;
        let currentImg = 0;
        const navItems = document.querySelectorAll('.nav-item');
        const img = document.getElementById('theme-img');

        function updateBlock() {
            img.style.opacity = 0.5;
            setTimeout(() => {
                img.src = groups[currentGroup].images[currentImg];
                img.style.opacity = 1;
            }, 120);
        }
        function setActiveNav() {
            navItems.forEach((item, idx) => {
                if(idx === currentGroup) item.classList.add('active');
                else item.classList.remove('active');
            });
        }
        navItems.forEach((item, idx) => {
            item.onclick = () => {
                currentGroup = idx;
                currentImg = 0;
                updateBlock();
                setActiveNav();
            }
        });
        img.onclick = () => {
            currentImg = (currentImg + 1) % groups[currentGroup].images.length;
            updateBlock();
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML, groups=portfolio_groups)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 