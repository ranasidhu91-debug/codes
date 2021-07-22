package game;

import edu.monash.fit2099.engine.*;

/**
 * Special class to Harvest Ripe food.
 */

public class HarvestAction extends Action {
    /**
     * Location to be harvested
     */
    protected Location target;

    /**
     * Constructor class
     * @param target The location to be harvested
     */
    public HarvestAction(Location target) {
        this.target = target;
    }

    /**
     * Performs the action of harvesting a ripened crop. If the actor has the ZombieCapability.FARM, it would harvest the
     * crop and drop the food to the ground. However, if the actor has a ZombieCapability.FOOD, it would harvest the crop
     * and store the food into it's inventory.
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return a description of what happened that can be displayed to the user
     */
    @Override
    public String execute(Actor actor, GameMap map){
        if(target.getGround().hasCapability(ZombieCapability.COMPLETE)){
            Food food = new Food("Food",'A');
            Dirt dirt = new Dirt();
            if(actor.hasCapability(ZombieCapability.FARM)){
                target.addItem(food);
                target.getGround().removeCapability(ZombieCapability.COMPLETE);
                target.getGround().removeCapability(ZombieCapability.FERTILIZE);
                target.setGround(dirt);
                return actor + " harvested food and dropped it to the ground";
            }
            if(actor.hasCapability(ZombieCapability.FOOD)){
                actor.addItemToInventory(food);
                target.removeItem(food);
                target.getGround().removeCapability(ZombieCapability.COMPLETE);
                target.getGround().removeCapability(ZombieCapability.FERTILIZE);
                target.setGround(dirt);
                return actor + " picked up harvested food";
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
        return actor + " can harvest crop for food";
    }
}