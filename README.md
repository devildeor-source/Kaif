<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLUMEN AI | Invest Your Time</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        :root {
            --bg-color: #0a0a0a;        /* Pitch Black background */
            --accent-blue: #2563eb;     /* Blue from your sketch */
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
            max-width: 400px; /* Kept narrow for the mobile view in your sketch */
            padding: 20px;
        }
        /* Top 'Kaif' and '<!DOCTYPE html>' section */
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
        /* Brand and Moto Section */
        .brand-title {
            font-size: 2.2rem;
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
        .cross { color: #ff4444; } /* Red X as in sketch */
        .check { color: var(--accent-blue); } /* Blue check as in sketch */
        /* --- Updated Pill-shaped Search Bar --- */
        .search-wrapper {
            display: flex;
            align-items: center;
            border: 2px solid var(--accent-blue); /* The distinct blue border from your drawing */
            border-radius: 50px;
            padding: 10px 15px; /* Adjust padding around icons */
            background: rgba(37, 99, 235, 0.05); /* Slight blue tint inside */
            position: relative;
        }
        /* Style for the 'Mic' button (Left) */
        #micBtn {
            background: none;
            border: none;
            color: var(--accent-blue);
            font-size: 1rem;
            cursor: pointer;
            padding: 0 10px;
        }
        /* The main input box 'Ask anything' */
        .search-wrapper input {
            flex: 1; /* Take up the remaining space */
            background: transparent;
            border: none;
            color: var(--text-white);
            font-size: 1rem;
            outline: none;
            font-weight: 500;
            padding: 0 5px;
        }
        .search-wrapper input::placeholder {
            color: var(--text-dim);
            opacity: 0.8;
        }
        /* --- Style for the 'Send' button (Right) - Updated --- */
        #solveBtn {
            background: none;
            border: none;
            color: var(--accent-blue); /* Same accent blue for a clean look */
            font-size: 1.5rem; /* Large and clear, just like the sketch */
            cursor: pointer;
            padding: 0 10px;
            transition: color 0.3s ease, transform 0.2s;
        }
        #solveBtn:hover {
            color: #fff; /* Turn white on hover to show it's interactive */
            transform: scale(1.1);
        }
        #solveBtn:active {
            transform: scale(0.95);
        }
        /* Logic part is unchanged */
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
            <button id="micBtn" onclick="startMic()"><i class="fa-solid fa-microphone"></i></button>            
            <input type="text" id="userInput" placeholder="Ask anything">          
            <button id="solveBtn" onclick="sendQuery()">
                <i class="fa-solid fa-arrow-up-circle"></i> </button>
        </div>
        <div id="response-box"></div>
    </div>
    <script>
        // No changes to logic, just UI fix
        async function sendQuery() {
            const input = document.getElementById('userInput').value;
            const resBox = document.getElementById('response-box');
            const sendIcon = document.querySelector('#solveBtn i'); // Reference the icon
            if(!input) return alert("Please enter a question!");
            // UI feedback while processing
            sendIcon.className = "fa-solid fa-spinner fa-spin"; // Change arrow to spinner
            resBox.style.display = 'block';
            resBox.innerText = "Analyzing numerical with Gemini...";
            try {
                const response = await fetch('/api/search', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: input})
                });
                const data = await response.json();
                resBox.innerText = data.solution;
            } catch (e) {
                resBox.innerText = "Error connecting to the LLUMEN API.";
            } finally {
                // Restore icon after processing
                sendIcon.className = "fa-solid fa-arrow-up-circle";
            }
        }
        // Logic integration for mic is complex and requires extra code, leaving placeholder
        function startMic() {
            alert("Microphone activation logic is not yet integrated. Requires additional libraries and permissions.");
        }
    </script>
</body>
</html>
