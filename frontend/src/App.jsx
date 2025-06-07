import { useState } from 'react';

function App() {
  const [slotsJson, setSlotsJson] = useState('');
  const [suggestedSlots, setSuggestedSlots] = useState([]);
  const [duration, setDuration] = useState(30);
  const [bookedUsers, setBookedUsers] = useState('');
  const [bookStart, setBookStart] = useState('');
  const [bookEnd, setBookEnd] = useState('');

  const handleSlotSubmit = async () => {
    try {
      const payload = JSON.parse(slotsJson);
      const res = await fetch('http://localhost:8000/slots', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      console.log(data);
      alert('Slots submitted!');
    } catch (err) {
      alert('Invalid JSON or request failed');
      console.error(err);
    }
  };

  const handleSuggest = async () => {
    const res = await fetch(`http://localhost:8000/suggest?duration=${duration}`);
    const data = await res.json();
    setSuggestedSlots(data.suggested_slots);
  };

  const handleBook = async () => {
    const payload = {
      user_ids: bookedUsers.split(',').map((id) => parseInt(id.trim())),
      start_time: bookStart,
      end_time: bookEnd,
    };

    const res = await fetch('http://localhost:8000/book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    alert(data.message);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Submit /slots</h2>
      <textarea
        rows="10"
        cols="50"
        value={slotsJson}
        onChange={(e) => setSlotsJson(e.target.value)}
      />
      <br />
      <button onClick={handleSlotSubmit}>Submit Slots</button>

      <h2>Get /suggest</h2>
      <label>Duration (min): </label>
      <input
        type="number"
        value={duration}
        onChange={(e) => setDuration(parseInt(e.target.value))}
      />
      <button onClick={handleSuggest}>Suggest</button>

      {suggestedSlots.length > 0 && (
        <>
          <h3>Available Time Slots</h3>
          <table border="1">
            <thead>
              <tr>
                <th>#</th>
                <th>Time Slot</th>
              </tr>
            </thead>
            <tbody>
              {suggestedSlots.map((slot, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{slot}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}

      <h2>Post /book</h2>
      <label>User IDs (comma separated): </label>
      <input value={bookedUsers} onChange={(e) => setBookedUsers(e.target.value)} />
      <br />
      <label>Start Time (HH:MM): </label>
      <input value={bookStart} onChange={(e) => setBookStart(e.target.value)} />
      <br />
      <label>End Time (HH:MM): </label>
      <input value={bookEnd} onChange={(e) => setBookEnd(e.target.value)} />
      <br />
      <button onClick={handleBook}>Book</button>
    </div>
  );
}

export default App;

