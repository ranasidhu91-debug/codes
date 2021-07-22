package game;

import edu.monash.fit2099.engine.*;

/**
 * A class to fertilize a crop.
 */

public class FertilizeAction extends Action {

    /**
     * The location of the crop that would be fertilized.
     */
    protected Ground target;

    public FertilizeAction(Ground target){
        this.target = target;
    }

    /**
     * Fertilizes a crop and adds the capability ZombieCapability.FERTILIZE
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return a description of what happened that can be displayed to the user
     */
    @Override
    public String execute(Actor actor, GameMap map){
        target.addCapability(ZombieCapability.FERTILIZE);
        return actor + " fertilized crop";
    }

    /**
     * Returns a descriptive String
     * @param actor The actor performing the action.
     * @return the text we put on the menu
     */
    @Override
    public String menuDescription(Actor actor){
        return actor + " fertilizes crop";
    }

}
