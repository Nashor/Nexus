package com.nashorsmind.nexus;

import org.bukkit.Location;

public class Nexus extends BlockLocation {

    private int minfluence, maxfluence;
    private int radius, radiusSquared;
    private double diffuse;
    
    private double a, b, c;
    
    public Nexus(Location location, int min, int max, int radius, double diffuse) {
        super(location);
        this.minfluence = min;
        this.maxfluence = max;
        this.radius = radius;
        this.radiusSquared = radius * radius;
        this.diffuse = diffuse;
        
        this.calculateConstants();
    }
    
    private void calculateConstants() {
        this.a = this.maxfluence - this.minfluence + this.diffuse;
        this.b = this.minfluence - this.diffuse;
        this.c = this.radiusSquared / Math.log(diffuse / this.a);
    }
    
    public double influence(Location location) {
        double distSquared = this.distSquared(location);
        
        if (distSquared > this.radiusSquared) {
            return 0;
        } else {
            return this.a * Math.exp(distSquared / this.c) + this.b;
        }
    }
    
    @Override
    public String toString() {
        return String.format(
            "Nexus=[%d,%d,%d](%d,%d,%d,%f)",
            this.getX(), this.getY(), this.getZ(),
            this.minfluence, this.maxfluence,
            this.radius,
            this.diffuse
        );
    }

}
