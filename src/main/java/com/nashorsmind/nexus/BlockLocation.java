package com.nashorsmind.nexus;

import org.bukkit.Location;

public class BlockLocation implements Comparable<Object> {
    
    private int x, y, z;
    
    public BlockLocation(Location location) {
        this.x = location.getBlockX();
        this.y = location.getBlockY();
        this.z = location.getBlockZ();
    }

    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
    
    public int getZ() {
        return this.z;
    }
    
    public double distSquared(BlockLocation location) {
        return (
            Math.pow(this.x - location.x, 2) + 
            Math.pow(this.y - location.y, 2) + 
            Math.pow(this.z - location.z, 2)
        );
    }
    
    public double distSquared(Location location) {
        return (
            Math.pow(this.x - location.getBlockX(), 2) + 
            Math.pow(this.y - location.getBlockY(), 2) + 
            Math.pow(this.z - location.getBlockZ(), 2)
        );
    }

    @Override
    public int compareTo(Object other) {
        int oX, oY, oZ;
        
        if (other instanceof BlockLocation) {
            BlockLocation location = (BlockLocation) other;
            oX = location.x;
            oY = location.y;
            oZ = location.z;
        } else if (other instanceof Location) {
            Location location = (Location) other;
            oX = location.getBlockX();
            oY = location.getBlockY();
            oZ = location.getBlockZ();
        } else {
            // The objects cannot be compared.
            return 0;
        }
        
        if (this.x == oX) {
            if (this.y == oY) {
                return this.z - oZ;
            } else {
                return this.y - oY;
            }
        } else {
            return this.x - oX;
        }
    }

}
