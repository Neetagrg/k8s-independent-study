from pymavlink import mavutil

log_file = "test_flight.bin"
mlog = mavutil.mavlink_connection(log_file)

print(f"--- 🚀 Analyzing Flight Data: {log_file} ---")

altitudes = []
count = 0

while True:
    msg = mlog.recv_match(type=['VFR_HUD', 'GLOBAL_POSITION_INT', 'HEARTBEAT'], blocking=False)
    if msg is None:
        break

    if msg.get_type() == 'VFR_HUD':
        altitudes.append(msg.alt)
        if len(altitudes) % 10 == 0:
            print(f"[NAV] Altitude: {msg.alt:.2f}m | Speed: {msg.airspeed:.2f}m/s")
    
    count += 1
    if count > 500: # Stop after 500 messages so it doesn't scroll forever
        break

print("\n--- 📊 Flight Summary ---")
if altitudes:
    print(f"Max Altitude: {max(altitudes):.2f}m")
    print(f"Min Altitude: {min(altitudes):.2f}m")
print("--- Analysis Complete ---")
