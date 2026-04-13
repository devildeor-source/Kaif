<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLUMEN AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        :root { --bg: #0a0a0a; --accent: #2563eb; --white: #ffffff; }
        body { background: var(--bg); color: var(--white); font-family: 'Inter', sans-serif; height: 100vh; display: flex; justify-content: center; align-items: center; margin: 0; }
        .container { text-align: center; width: 90%; max-width: 400px; }      
        /* UI Elements from your Sketch */
        .user-name { color: var(--accent); font-size: 2.5rem; margin-bottom: 5px; font-weight: 600; }
        .divider { width: 100px; height: 1px; background: #333; margin: 0 auto 15px; }
        .tagline { font-family: 'JetBrains Mono'; color: #666; font-size: 0.8rem; margin-bottom: 30px; }
        .brand { font-size: 2rem; letter-spacing: 4px; margin-bottom: 40px; text-transform: uppercase; }
        .moto { margin-bottom: 50px; text-transform: uppercase; font-size: 0.9rem; letter-spacing: 1px; font-weight: 300; }
        .moto div { margin: 10px 0; display: flex; justify-content: center; align-items: center; gap: 10px; }
        .cross { color: #ff4444; }
        .check { color: var(--accent); }
        /* --- THE CORRECTED PILL BAR --- */
        .search-pill { 
            display: flex; 
            align-items: center; 
            border: 2px solid var(--accent); 
            border-radius: 50px; 
            padding: 8px 12px; 
            background: rgba(37,99,235,0.05);
        }     
        .search-pill input { 
            flex: 1; 
            background: transparent; 
            border: none; 
            color: white; 
            outline: none; 
            font-size: 1rem; 
            padding: 0 10px;
        }
        /* The Send Button Circle from your drawing */
        .send-btn {
            background: none;
            border: none;
            color: var(--accent);
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
        }        
        .send-btn:active { transform: scale(0.9); }
        #response { margin-top: 30px; font-size: 0.9rem; color: #ccc; text-align: left; max-height: 200px; overflow-y: auto; display: none; padding: 10px; background: #111; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="user-name">Kaif</h1>
        <div class="divider"></div>
        <p class="tagline">&lt;!DOCTYPE html&gt;</p>      
        <h2 class="brand">LLUMEN AI</h2>     
        <div class="moto">
            <div>Spend your time <i class="fa-solid fa-xmark cross"></i></div>
            <div>Invest your time <i class="fa-solid fa-check check"></i></div>
        </div>
        <div class="search-pill">
            <button class="send-btn" onclick="startMic()"><i class="fa-solid fa-microphone"></i></button>
            <input type="text" id="userInput" placeholder="Ask anything">
            <button class="send-btn" onclick="sendQuery()">
                <i class="fa-solid fa-circle-arrow-up"></i>
            </button>
        </div>
        <div id="response"></div>
    </div>
    <script>
        async function sendQuery() {
            const query = document.getElementById('userInput').value;
            const res = document.getElementById('response');
            if(!query) return;
            res.style.display = 'block';
            res.innerText = "Analyzing...";
            try {
                const response = await fetch('/api/search', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: query})
                });
                const data = await response.json();
                res.innerText = data.solution;
            } catch (e) {
                res.innerText = "Error connecting to backend.";
            }
        }
        function startMic() {
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.onresult = (e) => {                document.getElementById('userInput').value = e.results[0][0].transcript; 
            };
            recognition.start();
        }
    </script>
</body>
</html>
