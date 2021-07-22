package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.List;

/**
 * A class that generates an EatAction.
 */
public class EatBehaviour implements Behaviour {
    private ZombieCapability whatever;

    /**
     * A Constructor that sets it such that the owner of this capability is allowed to eat.
     * @param whatever
     */
    public EatBehaviour(ZombieCapability whatever){
        this.whatever = whatever;
    }

    /**
     * Returns an EatAction that only allows a human with the same team as "Whatever" and an item with that same team as
     * "whatever" to be eaten.
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     *
     */
    @Override
    public Action getAction(Actor actor,GameMap map){
        List<Item> items = new ArrayList<Item>(actor.getInventory());
        if(actor.hasCapability(whatever)){
            for(Item item:items){
                if (item.hasCapability(whatever)){
                    return new EatAction(item);
                }
            }
        }
        return null;
    }
}
