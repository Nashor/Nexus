package com.nashorsmind.nexus;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.block.Block;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockBreakEvent;
import org.bukkit.event.block.BlockPlaceEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class NexusPlugin extends JavaPlugin implements Listener {
    
    private Database db = new Database();
    
    @Override
    public void onEnable() {
        this.getServer().getPluginManager().registerEvents(this, this);
        System.out.println("Nexus enabled!");
    }
    
    @Override
    public void onDisable() {
        System.out.println("Nexus disabled!");
    }
    
    @EventHandler
    public void onNexusPlace(BlockPlaceEvent event) {
        Block block = event.getBlock();
        if (block.getType() == Material.GLOWSTONE) {
            Nexus nexus = new Nexus(block.getLocation(), 5, 10, 5, 1.);
            if (this.db.addNexus(nexus) == true) {
                event.getPlayer().sendMessage(nexus.toString() + " placed!");                
            }
        }
    }
    
    @EventHandler
    public void onBlockBreak(BlockBreakEvent event) {
        Block block = event.getBlock();
        Location loc = block.getLocation();
        
        if (block.getType() == Material.GLOWSTONE) {
            Nexus nexus = this.db.getNexus(loc);
            if (this.db.removeNexus(nexus) == true) {
                event.getPlayer().sendMessage(nexus.toString() + " removed!");
            }
        } else {
            Nexus nexus = this.db.getTopInfluencer(loc);  
            if (nexus != null) {
                event.getPlayer().sendMessage(nexus.toString() + ", " + nexus.influence(loc));
            }
        }
    }
    
}
