# Import matplotlib for plotting, mdates for time formatting, pandas to read in csv data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
# Read in CSV
df = pd.read_csv('cmg_data_wheelspeed_1.0_CSV.csv')
# Format time datafield
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%m/%d/%Y %H:%M')





#################################################################################################################
#########################################  WHEEL SPEED VS TIME ##################################################
#################################################################################################################
# Plot Wheel Speed Over Time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('Wheel Speed Over Time')
plt.tight_layout()
plt.show()




#################################################################################################################
#########################################  WHEEL ACCELERATION VS POWER ##########################################
#################################################################################################################
# Plot Wheel Acceleration over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (rad/s²)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('Wheel Acceleration Over Time')
plt.tight_layout()
plt.show()




#################################################################################################################
##################################  WHEEL SPEED VS WHEEL ACCELERATION VS TIME ###################################
#################################################################################################################
#Plot Wheel Speed vs Acceleration Over Time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Acceleration (rad/s²)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & Acceleration Over Time')
plt.tight_layout()
plt.show()




#################################################################################################################
#########################################  WHEEL SPEED VS POWER #################################################
#################################################################################################################
#Plot Wheel speed vs 3.3v current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['cur_3v3_A'], label='Current (Amperes)', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 3.3V Current Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel Speed vs 5v Current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['cur_5V_A'], label='Current (Amperes)', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 5V Current Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel speed vs 3.3v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['vol_3v3_V'], label='Voltage V', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 3.3v Voltage Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel speed vs 5v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['vol_5V_V'], label='Voltage V', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 3.3v Voltage Over Time')
plt.tight_layout()
plt.show()




#################################################################################################################
#########################################  WHEEL ACCELERATION VS POWER ##########################################
#################################################################################################################
#Plot Wheel Acceleration vs 3.3v current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['cur_3v3_A'], label='Current (Amperes)', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3V Current Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel Acceleration Speed vs 5v Current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['cur_5V_A'], label='Current (Amperes)', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 5V Current Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel Acceleration vs 3.3v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['vol_3v3_V'], label='Voltage V', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3v Voltage Over Time')
plt.tight_layout()
plt.show()
#################################################################################################################
#Plot Wheel Acceleration vs 5v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['timestamp'], df['vol_5V_V'], label='Voltage V', color='C1', linestyle='--',)

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3v Voltage Over Time')
plt.tight_layout()
plt.show()