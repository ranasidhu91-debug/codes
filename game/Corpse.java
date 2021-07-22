package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * Base Class for all corpses that would turn into a zombie after 5-10 turns.
 */

public class Corpse extends PortableItem {
    /**
     * Constructor class for creating a corpse
     * @param name The Corpse's display name
     * @param displayChar Character the corpse would be recognized by.
     */
    public Corpse(String name,char displayChar){
        super(name,displayChar);
        addCapability(ZombieCapability.RISE);
    }

    private Display display = new Display();
    int min = 5;
    int max = 10;
    Random rand = new Random();
    int randomNum = rand.nextInt((max-min) + 1) + min;
    int transform = 0;

    /**
     * Allows the corpse to feel the passage of time when it is lying on the ground. After about 5-10 turns, the corpse
     * would rise again as a Zombie.
     * @param location Location the corpse is at.
     */
    @Override
    public void tick(Location location){
        super.tick(location);
        transform ++;
        if(transform == randomNum){
            Zombie zombie = new Zombie("Corpse-Zombie");
            location.removeItem(this);
            location.addActor(zombie);
            display.println("Corpse became a zombie");
        }
    }

    /**
     * Allows the corpse that has been picked up by human to feel the passage of time. After the human has carried the
     * corpse for about 5-10 turns, the corpse has become a Zombie and be dropped to the nearest location from the actor.
     * @param location The location of the actor.
     * @param actor The actor carrying this Item.
     */
    @Override
    public void tick(Location location,Actor actor){
        super.tick(location,actor);
        transform ++;
        if(transform == randomNum){
            List<Item> items = actor.getInventory();
            List<Exit> exits = new ArrayList<>(location.getExits());
            Collections.shuffle(exits);
            Exit droppedZombie = exits.get(0);
            for(Item item : items){
                if(item.hasCapability(ZombieCapability.RISE)){
                    Zombie zombie = new Zombie("Corpse-Zombie");
                    droppedZombie.getDestination().addActor(zombie);
                    actor.removeItemFromInventory(item);
                    new DropItemAction(item);
                    display.println(actor + " dropped corpse as it is a zombie.");
                    break;
                }
            }
        }
    }
}
