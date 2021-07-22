package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


/**
 * A class that generates an CraftAction if the current Actor has items.
 *
 *
 * @author Seth
 *
 */
public class CraftBehaviour implements Behaviour {
    private ZombieCapability capability;
    private final ZombieCapability CRAFTABLE = ZombieCapability.CRAFTABLE;

    /**
     * Constructor
     * Sets the team to CRAFT, allowing humans to craft
     * @param capability Team descriptor of Actor to craft
     */
    public CraftBehaviour(ZombieCapability capability){
        this.capability = capability;
    }


    /**
     * Check actor(Humans) inventory, and crafts the first item that is craftable in the inventory
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     * @return a new CraftAction with the craftable item
     */
    public Action getAction(Actor actor,GameMap map){
        List <Item> inventory = actor.getInventory();
        if (actor.hasCapability(capability)) {
            for (Item item : inventory) {
                if (item.hasCapability(CRAFTABLE)) {
                    return new CraftAction(item);
                }
            }
        }
        return null;
    }
}
