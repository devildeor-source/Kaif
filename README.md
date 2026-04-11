<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLUMEN AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #0a0a0a;        /* Pitch Black */
            --accent-blue: #2563eb;     /* The blue from your sketch */
            --text-white: #ffffff;
            --text-dim: #a0a0a0;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-white);
            font-family: 'Inter', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .container {
            text-align: center;
            width: 100%;
            max-width: 400px;
            padding: 20px;
        }
        .user-name {
            color: var(--accent-blue);
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 5px;
        }
        .divider {
            width: 120px;
            height: 1px;
            background: #444;
            margin: 0 auto 20px auto;
        }
        .tagline {
            font-family: 'JetBrains Mono', monospace;
            color: #888;
            font-size: 0.9rem;
            margin-bottom: 30px;
        }
        .brand-title {
            font-size: 2rem;
            letter-spacing: 5px;
            font-weight: 400;
            margin-bottom: 40px;
            text-transform: uppercase;
        }
        .moto-container {
            margin-bottom: 60px;
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .moto-row {
            margin: 10px 0;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
        }

        .cross { color: #ff4444; }
        .check { color: var(--accent-blue); }

        /* The Pill-shaped Search Bar from your sketch */
        .search-wrapper {
            display: flex;
            align-items: center;
            border: 2px solid var(--accent-blue);
            border-radius: 50px;
            padding: 12px 20px;
            background: rgba(37, 99, 235, 0.05);
        }

        .search-wrapper input {
            flex: 1;
            background: transparent;
            border: none;
            color: var(--accent-blue);
            font-size: 1rem;
            text-transform: uppercase;
            outline: none;
            font-weight: 500;
        }

        .search-wrapper input::placeholder {
            color: var(--accent-blue);
            opacity: 0.7;
        }

        .icon-btn {
            background: none;
            border: none;
            color: var(--accent-blue);
            font-size: 1.2rem;
            cursor: pointer;
            margin: 0 5px;
        }

        #response-box {
            margin-top: 30px;
            font-size: 0.9rem;
            color: #ccc;
            max-height: 150px;
            overflow-y: auto;
            display: none;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1 class="user-name">Kaif</h1>
        <div class="divider"></div>
        <p class="tagline">&lt;!DOCTYPE html&gt;</p>

        <h2 class="brand-title">LLUMEN AI</h2>

        <div class="moto-container">
            <div class="moto-row">
                <span>Spend your time</span>
                <i class="fa-solid fa-xmark cross"></i>
            </div>
            <div class="moto-row">
                <span>Invest your time</span>
                <i class="fa-solid fa-check check"></i>
            </div>
        </div>

        <div class="search-wrapper">
            <button class="icon-btn" onclick="startMic()"><i class="fa-solid fa-microphone"></i></button>
            <input type="text" id="userInput" placeholder="Ask anything">
            <button class="icon-btn" onclick="sendQuery()"><i class="fa-solid fa-arrow-up-circle"></i></button>
        </div>

        <div id="response-box"></div>
    </div>

    <script>
        async function sendQuery() {
            const input = document.getElementById('userInput').value;
            const resBox = document.getElementById('response-box');
            if(!input) return;

            resBox.style.display = 'block';
            resBox.innerText = "Processing...";

            try {
                const response = await fetch('/api/search', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: input})
                });
                const data = await response.json();
                resBox.innerText = data.solution;
            } catch (e) {
                resBox.innerText = "Error connecting to server.";
            }
        }

        function startMic() {
            alert("Microphone activated (Logic integration needed)");
        }
    </script>

</body>
</html>
