# BB84 Quantum Key Simulator

## How It Works 

1. **Alice sends signals:** Alice generates random bits (0s and 1s) and sends them using random filters (`R` or `D`).
2. **Bob reads the signals:** Bob chooses his own random filters (`R` or `D`) to read what Alice sent.
3. **They compare filters:** Alice and Bob publicly check which filters they had in common. When their filters match, their bits match too. They keep these matching bits as their secret key.
4. **Catching the spy:**
* **Normal Run:** No spy. Alice and Bob get the exact same bits (**0% errors**).
* **Under Attack:** Eve tries to spy in the middle. In quantum physics, looking at a signal changes it. Eve's presence scrambles the bits, causing errors (**around 25% errors**). Alice and Bob instantly know someone is listening and discard the key.

---

## Requirements
* Having a computer.
* **Python 3** installed on your computer, nothing else.

---

## How to Run

1. Open your terminal or command prompt in the folder where is **tarea6.py**.
2. Run:

```bash
python bb84.py

```

---

## Understanding the Output

The program runs both situations back-to-back:

* **Normal Run (`simulacion_caso_normal`):**
* **Errors:** `0`
* **Error Rate:** `0.0` (0%)
* *Meaning:* The channel is completely secure. Alice and Bob have an identical secret key.


* **Under Attack (`simulacion_bajo_ataque`):**
* **Errors:** Around 10 to 15 (out of a 50-bit test sample).
* **Error Rate:** Around `0.25` (25%).
* *Meaning:* Eve got caught! Alice and Bob know the channel was tapped.



---

## Files Generated

The script automatically saves text files so you can open them and inspect the data:

| File | What is inside |
| --- | --- |
| `alice_bb84.txt` | Alice's original bits and filters (normal run). |
| `bob_bb84.txt` | Bob's received bits and filters (normal run). |
| `alice_bb84_attack.txt` | Alice's bits and filters during the attack. |
| `eve_bb84_attack.txt` | The bits and filters Eve intercepted. |
| `bob_bb84_attack.txt` | The corrupted bits Bob received after Eve interfered. |
