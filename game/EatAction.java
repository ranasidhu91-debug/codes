package game;

import edu.monash.fit2099.engine.*;

/**
 * Special class for eating.
 */

public class EatAction extends Action {
    /**
     * The item to be eaten
     */
    protected Item target;

    public EatAction(Item target){
        this.target = target;
    }

    /**
     * Performs the action. For the food to be eaten, the food must have the ZombieCapability.FOOD and the human
     * must have either ZombieCapability.FOOD or ZombieCapability.FARM
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return A description of what happened that would be displayed to the user.
     */
    @Override
    public String execute(Actor actor, GameMap map){
        if(target.hasCapability(ZombieCapability.FOOD)){
            if(actor.hasCapability(ZombieCapability.FOOD)||actor.hasCapability(ZombieCapability.FARM)){
                actor.removeItemFromInventory(target);
                actor.heal(10);
                return actor + " ate food and healed by 10 points";
            }
        }
        return null;
    }

    /**
     * Returns a descriptive String
     * @param actor The actor performing the action.
     * @return the text we put on the menu
     */
    @Override
    public String menuDescription(Actor actor){
        return actor + " can eat food to restore health";
    }

}
