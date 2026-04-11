<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Physics Support AI | Solved Numericals</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0d0d0d;        /* Deep Matte Black */
            --card-bg: #161616;        /* Slightly lighter black for cards */
            --accent-color: #00f2ff;    /* Neon Cyan */
            --text-main: #e0e0e0;
            --text-dim: #888888;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .dashboard {
            width: 100%;
            max-width: 800px;
            background: var(--card-bg);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
            border: 1px solid #222;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        header h1 {
            font-weight: 600;
            font-size: 2rem;
            letter-spacing: -1px;
            background: linear-gradient(to right, #fff, var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        header p {
            color: var(--text-dim);
            font-size: 0.9rem;
            margin-top: 10px;
        }

        .search-section {
            position: relative;
            margin-bottom: 30px;
        }

        input[type="text"] {
            width: 100%;
            background: #1e1e1e;
            border: 1px solid #333;
            padding: 18px 25px;
            border-radius: 12px;
            color: white;
            font-size: 1rem;
            transition: all 0.3s ease;
            outline: none;
        }

        input[type="text"]:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        }

        button {
            width: 100%;
            margin-top: 15px;
            background: var(--accent-color);
            color: #000;
            border: none;
            padding: 15px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
        }

        button:active {
            transform: scale(0.98);
        }

        #result-container {
            margin-top: 40px;
            display: none;
            animation: fadeIn 0.5s ease;
        }

        .result-card {
            background: #1a1a1a;
            border-left: 4px solid var(--accent-color);
            padding: 25px;
            border-radius: 8px;
        }

        .result-card h3 {
            font-size: 0.8rem;
            text-transform: uppercase;
            color: var(--accent-color);
            margin-bottom: 15px;
            letter-spacing: 1px;
        }

        .solution-text {
            font-family: 'JetBrains Mono', monospace;
            line-height: 1.6;
            color: #ccc;
            white-space: pre-line;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Admin Link Style */
        .admin-btn {
            display: block;
            text-align: center;
            margin-top: 30px;
            color: var(--text-dim);
            text-decoration: none;
            font-size: 0.8rem;
            transition: color 0.3s;
        }

        .admin-btn:hover {
            color: var(--accent-color);
        }
    </style>
</head>
<body>

    <div class="dashboard">
        <header>
            <h1>Physics Support AI</h1>
            <p>Enter your numerical and let the AI solve it step-by-step.</p>
        </header>

        <div class="search-section">
            <input type="text" id="query" placeholder="e.g. Calculate the force if mass is 10kg and acceleration is 5m/s²">
            <button onclick="solveProblem()" id="solveBtn">Solve Numerical</button>
        </div>

        <div id="result-container">
            <div class="result-card">
                <h3>Solved Solution</h3>
                <div class="solution-text" id="solutionText">
                    </div>
            </div>
        </div>

        <a href="/admin" class="admin-btn">Access Admin Dashboard</a>
    </div>

    <script>
        async function solveProblem() {
            const query = document.getElementById('query').value;
            const btn = document.getElementById('solveBtn');
            const resultContainer = document.getElementById('result-container');
            const solutionText = document.getElementById('solutionText');

            if (!query) return alert("Please enter a question!");

            // UI Loading state
            btn.innerText = "Analyzing...";
            btn.style.opacity = "0.7";

            try {
                const response = await fetch('/api/search', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });

                const data = await response.json();

                resultContainer.style.display = 'block';
                solutionText.innerText = data.solution || data.message;
            } catch (error) {
                alert("Error connecting to the server.");
            } finally {
                btn.innerText = "Solve Numerical";
                btn.style.opacity = "1";
            }
        }
    </script>
</body>
</html>
