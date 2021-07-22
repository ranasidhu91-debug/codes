package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * A class that generates either a PickUpitem action or DropItem Action.
 */
public class PickDropBehaviour implements Behaviour{
    public ZombieCapability whatever;

    /**
     * A constructor that sets it such that only actors in the "whatever" team can pick up or drop portable items.
     * @param whatever
     */
    public PickDropBehaviour(ZombieCapability whatever){
        this.whatever = whatever;
    }

    /**
     * Returns a PickUpItem action or DropItem action randomly. Only if the actor has the capability "whatever" can perform
     * these actions.
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     */
    @Override
    public Action getAction(Actor actor, GameMap map){
        List<Item> items = new ArrayList<>(map.locationOf(actor).getItems());
        if(actor.hasCapability(whatever)){
            Random rand = new Random();
            boolean val = rand.nextBoolean();
            if(val){
                for (Item item:items){
                    if ((item.asWeapon() == null)){
                        List <Item> inventory = actor.getInventory();
                        if(!inventory.contains(item)){
                            return new PickUpItemAction(item);
                        }
                    }else{
                        if(actor instanceof Player){
                            List <Item> inventory = actor.getInventory();
                            if(!inventory.contains(item)){
                                return new PickUpItemAction(item);
                            }
                        }
                    }
                }
            }
            if(items.isEmpty()){
                List <Item> inventory = actor.getInventory();
                if(!inventory.isEmpty()){
                    Collections.shuffle(inventory);
                    Item item = inventory.get(rand.nextInt(inventory.size()));
                    return new DropItemAction(item);
                }
            }
        }
        return null;
    }
}
