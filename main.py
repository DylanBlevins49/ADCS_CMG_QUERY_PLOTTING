# Import matplotlib for plotting, mdates for time formatting, pandas to read in csv data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
# Read in CSV
df = pd.read_csv('cmg_data_wheelspeed_1.0.csv')
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
fig.savefig('wheel_speed_vs_time_0_5.png', dpi=300, bbox_inches='tight')




#################################################################################################################
#########################################  WHEEL ACCELERATION VS TIME ##########################################
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
fig.savefig('acceleration_vs_time_0_5.png', dpi=300, bbox_inches='tight')



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
fig.savefig('wheel_speed_vs_acceleration_vs_time_0_5.png', dpi=300, bbox_inches='tight')



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
fig.savefig('wheel_speed_vs_3v3_A_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('wheel_speed_vs_5v_A_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('wheel_speed_vs_3v3_V_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('wheel_speed_vs_5v_V_0_5.png', dpi=300, bbox_inches='tight')



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
fig.savefig('acceleration_vs_3v3_A_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('acceleration_vs_5v_A_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('acceleration_vs_3v3_V_0_5.png', dpi=300, bbox_inches='tight')
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
fig.savefig('acceleration_vs_5v_V_0_5.png', dpi=300, bbox_inches='tight')



#################################################################################################################
#########################################  POWER VS TIME ########################################################
#################################################################################################################
# Plot 3v3 A over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['cur_3v3_A'], label='Current (Amperes)')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('3.3v Current vs Time')
plt.tight_layout()
plt.show()
fig.savefig('3v3_A_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 5v A over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['cur_5V_A'], label='Current (Amperes)')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('5v Current vs Time')
plt.tight_layout()
plt.show()
fig.savefig('5v_A_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 3v3 V over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['vol_3v3_V'], label='Voltage V')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()

plt.title('3.3v Voltage vs Time')
plt.tight_layout()
plt.show()
fig.savefig('3v3_V_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 5v V over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['timestamp'], df['vol_5V_V'], label='Voltage V')

# create exactly 20 tick positions from start to end
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax1.set_xticks(ticks)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# labels & combined legend
ax1.set_xlabel('Time')
ax1.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()

plt.title('5v Voltage vs Time')
plt.tight_layout()
plt.show()
fig.savefig('5v_V_vs_time_1_0.png', dpi=300, bbox_inches='tight')



#################################################################################################################
###################################  TOTAL POWER CONSUMPTION VS TIME ############################################
#################################################################################################################
df['P_3v3_W'] = df['cur_3v3_A'] * df['vol_3v3_V']
df['P_5v_W']  = df['cur_5V_A']  * df['vol_5V_V']
df['P_total_W'] = df['P_3v3_W'] + df['P_5v_W']


fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(df['timestamp'], df['P_3v3_W'], label='3.3 V Rail Power')
ax.plot(df['timestamp'], df['P_5v_W'],  label='5 V Rail Power',   linestyle='--')
ax.plot(df['timestamp'], df['P_total_W'], label='Total Power',      linewidth=2)


# 3) force exactly 30 ticks
ticks = pd.date_range(df['timestamp'].min(),
                      df['timestamp'].max(),
                      periods=30)
ax.set_xticks(ticks)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))

yticks = np.arange(0, 8, 0.5)
ax.set_yticks(yticks)

# 4) rotate & label
plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
ax.set_xlabel('Time')
ax.set_ylabel('Power (W)')
ax.set_title('Rail Power and Total Power Consumption Over Time')
ax.legend(loc='upper right')


plt.tight_layout()
plt.show()
fig.savefig('Total_Power_vs_Time_1_0.png', dpi=300, bbox_inches='tight')