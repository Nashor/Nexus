package com.nashorsmind.nexus;

import java.util.ArrayList;
import java.util.Collections;

import org.bukkit.Location;

public class Database {
    
    private ArrayList<Nexus> nexusList = new ArrayList<Nexus>();
    
    public Database() {
        
    }
    
    public boolean addNexus(Nexus nexus) {
        int index = Collections.binarySearch(this.nexusList, nexus);
        
        if (index < 0) {
            this.nexusList.add(-(index + 1), nexus);
            return true;
        } else {
            return false;
        }
    }
    
    public boolean removeNexus(Nexus nexus) {
        int index = Collections.binarySearch(this.nexusList, nexus);
        
        if (index >= 0) {
            this.nexusList.remove(index);
            return true;
        } else {
            return false;
        }
    }
    
    public Nexus getNexus(Location loc) {
        int index = Collections.binarySearch(this.nexusList, loc);
        
        if (index >= 0) {
            return this.nexusList.get(index);
        } else {
            return null;
        }
    }
    
    public Nexus getTopInfluencer(Location loc) {
        Nexus topInfluencer = null;
        double topInfluence = 0.;
        
        for (Nexus nexus : this.nexusList) {
            if (nexus.influence(loc) > topInfluence) {
                topInfluencer = nexus;
                topInfluence = nexus.influence(loc);
            }
        }
        
        return topInfluencer;
    }

}
