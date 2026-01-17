#!/usr/bin/env python3
"""
Plot AI Location positions from AILocationSettings.json on an X/Y scatter plot.
Labels each point with its location name.
"""

import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from datetime import datetime
from pathlib import Path

def plot_ai_locations(json_file_path, output_dir=None):
    """
    Read AILocationSettings.json and create an X/Y scatter plot of all locations.

    Args:
        json_file_path: Path to the AILocationSettings.json file
        output_dir: Directory to save the output image (defaults to current directory)
    """
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Extract location data
    locations = data.get('RoamingLocations', [])

    if not locations:
        print("No locations found in the JSON file!")
        return

    # Extract X, Y coordinates, names, and radius values
    x_coords = []
    y_coords = []
    names = []
    radii = []

    for location in locations:
        position = location.get('Position', [])
        name = location.get('Name', 'Unknown')
        radius = location.get('Radius', 100.0)  # Default to 100 if not specified

        if len(position) >= 3:
            x = position[0]  # First coordinate
            y = position[2]  # Third coordinate (middle is always 0)

            x_coords.append(x)
            y_coords.append(y)
            names.append(name)
            radii.append(radius)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)  # 1000x1000 pixels (10 inches * 100 dpi)

    # Draw circles with actual radius values (in data coordinates = meters)
    for i in range(len(x_coords)):
        circle = Circle((x_coords[i], y_coords[i]), radii[i],
                       fill=True, facecolor='red', alpha=0.3,
                       edgecolor='darkred', linewidth=1.5)
        ax.add_patch(circle)

    # Plot center points for visibility
    ax.scatter(x_coords, y_coords, c='red', s=20, alpha=0.8, edgecolors='black', linewidth=0.5, zorder=5)

    # Add labels for each point
    for i, name in enumerate(names):
        ax.annotate(name, (x_coords[i], y_coords[i]),
                   fontsize=6,
                   alpha=0.8,
                   xytext=(3, 3),  # Offset text slightly from point
                   textcoords='offset points',
                   zorder=6)

    # Set labels and title
    ax.set_xlabel('X Coordinate (meters)', fontsize=12)
    ax.set_ylabel('Y Coordinate (meters)', fontsize=12)
    ax.set_title('AI Location Positions (circles show radius)', fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, alpha=0.3, linestyle='--')

    # Set axis limits to show full map (0-12800 meters) with some padding
    ax.set_xlim(-500, 13000)
    ax.set_ylim(-500, 13000)

    # Make sure the plot is square with equal aspect ratio
    ax.set_aspect('equal', adjustable='box')

    # Generate timestamp for filename
    timestamp = datetime.now().strftime('%Y%m%d%H%M')
    output_filename = f'AILocationsPlots-{timestamp}.png'

    # Determine output path
    if output_dir:
        output_path = Path(output_dir) / output_filename
    else:
        output_path = Path(output_filename)

    # Save the figure
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    print(f"Plot saved to: {output_path}")
    print(f"Total locations plotted: {len(names)}")

    # Close the plot to free memory
    plt.close()

if __name__ == '__main__':
    # Default path to AILocationSettings.json
    # Adjust this path if running from a different location
    json_path = Path(__file__).parent.parent / 'mpmissions' / 'dayzOffline.enoch' / 'expansion' / 'settings' / 'AILocationSettings.json'

    # Output to the custom_scripts directory
    output_directory = Path(__file__).parent

    print(f"Reading AI locations from: {json_path}")
    plot_ai_locations(json_path, output_directory)
