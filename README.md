<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLUMEN AI | Invest Your Time</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
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
            font-size: 2.2rem;
            letter-spacing: -1px;
            text-transform: uppercase; /* Match your sketch */
            background: linear-gradient(to right, #fff, var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Updated Moto Section to match your sketch */
        .moto {
            color: var(--text-dim);
            font-size: 0.9rem;
            margin-top: 15px;
            display: flex;
            flex-direction: column;
            gap: 5px;
            align-items: center;
        }

        .moto-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .fa-xmark {
            color: #ff4d4d; /* Red for cross */
        }

        .fa-check {
            color: var(--accent-color); /* Cyan for check */
        }

        /* Input area styled to match your sketch */
        .search-container {
            position: relative;
            margin-bottom: 30px;
        }

        .search-wrapper {
            position: relative;
            display: flex;
            align-items: center;
            background: #1e1e1e;
            border: 1px solid #333;
            border-radius: 12px;
            overflow: hidden; /* Important for icons */
        }

        .search-icon {
            padding: 0 15px;
            color: var(--text-dim);
            font-size: 1.1rem;
        }

        input[type="text"] {
            flex-grow: 1;
            background: transparent;
            border: none;
            padding: 18px 5px; /* Adjust padding around icons */
            color: white;
            font-size: 1rem;
            outline: none;
            font-family: 'Inter', sans-serif;
        }

        input[type="text"]::placeholder {
            color: var(--text-dim);
        }

        .search-wrapper:focus-within {
            border-color: var(--accent-color);
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        }

        /* Stylized Send Button */
        #solveBtn {
            background: none;
            border: none;
            color: var(--accent-color);
            padding: 0 20px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
        }

        #solveBtn:active {
            transform: scale(1.1);
        }

        /* Mic Button */
        #micBtn {
            background: none;
            border: none;
            color: var(--text-dim);
            padding: 0 5px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: color 0.3s;
        }

        #micBtn:hover {
            color: var(--accent-color);
        }

        /* --- Rest of the style unchanged --- */
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
            
