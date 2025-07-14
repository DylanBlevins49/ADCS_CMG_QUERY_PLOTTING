# Import matplotlib for plotting, mdates for time formatting, pandas to read in csv data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Read in CSV
df = pd.read_csv('random_wheel_speed_data.csv')
# Format time datafield
df['timestamp'] = pd.to_datetime(df['timestamp'],infer_datetime_format=True)
# Compute elapsed time for X axis ticks
start = df['timestamp'].iloc[0]
df['elapsed_s'] = (df['timestamp'] - start).dt.total_seconds()

# Helper Functions for X axis formatting
def mmss(x, pos):
    m, s = divmod(int(x), 60)
    return f"{m:d}:{s:02d}"

def format_elapsed_axis(ax, duration_s=600, interval_s=20):
    # 1) Set ticks at [0, 20, 40, …, duration_s]
    ax.set_xticks(np.arange(0, duration_s + 1, interval_s))
    # 2) Use our mm:ss formatter
    ax.xaxis.set_major_formatter(FuncFormatter(mmss))
    # 3) Rotate labels so they don’t overlap
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')


#################################################################################################################
#########################################  WHEEL SPEED VS TIME ##################################################
#################################################################################################################
# Plot Wheel Speed Over Time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(100, 160)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(5))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('Wheel Speed Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_time_0_5.png', dpi=300, bbox_inches='tight')




#################################################################################################################
#########################################  WHEEL ACCELERATION VS TIME ##########################################
#################################################################################################################
# Plot Wheel Acceleration over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(-100, 150)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(25))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Acceleration (rad/s²)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('Wheel Acceleration Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('acceleration_vs_time_0_5.png', dpi=300, bbox_inches='tight')



#################################################################################################################
##################################  WHEEL SPEED VS WHEEL ACCELERATION VS TIME ###################################
#################################################################################################################
#Plot Wheel Speed vs Acceleration Over Time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# custom‐scale left axis
ax2.set_ylim(-100, 150)
ax2.yaxis.set_major_locator(MultipleLocator(25))

# custom-scale right axis
ax1.set_ylim(100, 160)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(5))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Acceleration (rad/s²)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & Acceleration Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_acceleration_vs_time_0_5.png', dpi=300, bbox_inches='tight')



#################################################################################################################
#########################################  WHEEL SPEED VS POWER #################################################
#################################################################################################################
#Plot Wheel speed vs 3.3v current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['cur_3v3_A'], label='Current (Amperes)', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# custom‐scale left axis
ax1.set_ylim(100, 160)
ax1.yaxis.set_major_locator(MultipleLocator(5))

# custom‐scale right axis
ax2.set_ylim(0, 1)
ax2.yaxis.set_major_locator(MultipleLocator(0.1))


# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 3.3V Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_3v3_A_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel Speed vs 5v Current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['cur_5V_A'], label='Current (Amperes)', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# custom‐scale left axis
ax1.set_ylim(100, 160)
ax1.yaxis.set_major_locator(MultipleLocator(5))

# custom‐scale right axis
ax2.set_ylim(0, 2)
ax2.yaxis.set_major_locator(MultipleLocator(0.2))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 5V Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_5v_A_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel speed vs 3.3v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['vol_3v3_V'], label='Voltage V', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# custom‐scale left axis
ax1.set_ylim(100, 160)
ax1.yaxis.set_major_locator(MultipleLocator(5))

# custom‐scale right axis
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 3.3v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_3v3_V_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel speed vs 5v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_speed_hz'], label='Wheel Speed (Hz)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['vol_5V_V'], label='Voltage V', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# custom‐scale left axis
ax1.set_ylim(100, 160)
ax1.yaxis.set_major_locator(MultipleLocator(5))

# custom‐scale right axis
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Wheel Speed (Hz)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Speed & 5v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('wheel_speed_vs_5v_V_0_5.png', dpi=300, bbox_inches='tight')



#################################################################################################################
#########################################  WHEEL ACCELERATION VS POWER ##########################################
#################################################################################################################
#Plot Wheel Acceleration vs 3.3v current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['cur_3v3_A'], label='Current (Amperes)', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(-100, 150)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(25))

# custom‐scale right axis
ax2.set_ylim(0, 1)
ax2.yaxis.set_major_locator(MultipleLocator(0.1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3V Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('acceleration_vs_3v3_A_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel Acceleration Speed vs 5v Current over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['cur_5V_A'], label='Current (Amperes)', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(-100, 150)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(25))

# custom‐scale right axis
ax2.set_ylim(0, 2)
ax2.yaxis.set_major_locator(MultipleLocator(0.2))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 5V Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('acceleration_vs_5v_A_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel Acceleration vs 3.3v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['vol_3v3_V'], label='Voltage V', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(-100, 150)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(25))

# custom‐scale right axis
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('acceleration_vs_3v3_V_0_5.png', dpi=300, bbox_inches='tight')
#################################################################################################################
#Plot Wheel Acceleration vs 5v voltage over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['wheel_accel_rad_s2'], label='Acceleration (rad/s²)')
ax2 = ax1.twinx()
ax2.plot(df['elapsed_s'], df['vol_5V_V'], label='Voltage V', color='C1',)

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(-100, 150)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(25))

# custom‐scale right axis
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Acceleration (rad/s²)')
ax2.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()
l2, l2lab = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + l2lab, loc='upper left')

plt.title('Wheel Acceleration & 3.3v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('acceleration_vs_5v_V_0_5.png', dpi=300, bbox_inches='tight')



#################################################################################################################
#########################################  POWER VS TIME ########################################################
#################################################################################################################
# Plot 3v3 A over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['cur_3v3_A'], label='Current (Amperes)')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(0, 1)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(0.1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('3.3v Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('3v3_A_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 5v A over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['cur_5V_A'], label='Current (Amperes)')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(0, 2)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(0.2))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Current (Amperes)')
lines, labels = ax1.get_legend_handles_labels()

plt.title('5v Current Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('5v_A_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 3v3 V over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['vol_3v3_V'], label='Voltage V')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(0, 10)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()

plt.title('3.3v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('3v3_V_vs_time_1_0.png', dpi=300, bbox_inches='tight')
#################################################################################################################
# Plot 5v V over time
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df['elapsed_s'], df['vol_5V_V'], label='Voltage V')

# use helper to format X axis
format_elapsed_axis(ax1)

# Set custom Y axis scaling
ax1.set_ylim(0, 10)
# scaling for ticks, every x between range
ax1.yaxis.set_major_locator(MultipleLocator(1))

# labels & combined legend
ax1.set_xlabel('Time (mm:ss)')
ax1.set_ylabel('Voltage V')
lines, labels = ax1.get_legend_handles_labels()

plt.title('5v Voltage Over 10 Minutes')
plt.tight_layout()
plt.show()
# fig.savefig('5v_V_vs_time_1_0.png', dpi=300, bbox_inches='tight')




#################################################################################################################
###################################  TOTAL POWER CONSUMPTION VS TIME ############################################
#################################################################################################################
df['P_3v3_W'] = df['cur_3v3_A'] * df['vol_3v3_V']
df['P_5v_W']  = df['cur_5V_A']  * df['vol_5V_V']
df['P_total_W'] = df['P_3v3_W'] + df['P_5v_W']


fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(df['elapsed_s'], df['P_3v3_W'], label='3.3 V Rail Power')
ax.plot(df['elapsed_s'], df['P_5v_W'],  label='5 V Rail Power',)
ax.plot(df['elapsed_s'], df['P_total_W'], label='Total Power',linewidth=2)


# use helper to format X axis
format_elapsed_axis(ax)

# Yaxis Scaling (min, max, interval)
yticks = np.arange(0, 8, 0.5)
ax.set_yticks(yticks)

# label
ax.set_ylabel('Power (W)')
ax.set_title('Rail Power and Total Power Consumption Over 10 Minutes')
ax.legend(loc='upper right')


plt.tight_layout()
plt.show()
# fig.savefig('Total_Power_vs_Time_1_0.png', dpi=300, bbox_inches='tight')