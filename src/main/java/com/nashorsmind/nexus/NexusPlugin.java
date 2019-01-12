package com.nashorsmind.nexus;

import org.bukkit.plugin.java.JavaPlugin;

public class NexusPlugin extends JavaPlugin {
    
    @Override
    public void onEnable() {
        System.out.println("Nexus enabled!");
    }
    
    @Override
    public void onDisable() {
        System.out.println("Nexus disabled!");
    }
}
