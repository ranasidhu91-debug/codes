package game;

import edu.monash.fit2099.engine.*;

/**
 * Action for crafting
 */
public class CraftAction extends Action{

    /**
     * Stores the item that is to be crafted
     */
    protected Item item;

    /**
     * Constructor that will take the item to be crafted and assign it to the protected variable item.
     * @param itemToCraft item to be crafted
     */
    public CraftAction(Item itemToCraft) {
        this.item = itemToCraft;
    }


    /**
     * Will check the name of the to be crafted item and remove the item from inventory to add
     * the new crafted item to the inventory
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return a String stating the actor has crafted which item into which
     */
    public String execute(Actor actor, GameMap map){
        String newWeapon = "";
        if (this.item.toString().equals("Zombie Arm")) {
            actor.removeItemFromInventory(this.item);
            actor.addItemToInventory(new ZombieClub());
            newWeapon = new ZombieClub().toString();
        } else if (this.item.toString().equals("Zombie Leg")) {
            actor.removeItemFromInventory(this.item);
            actor.addItemToInventory(new ZombieMace());
            newWeapon = new ZombieMace().toString();
        }
        return actor + " crafted " + this.item.toString() + " into a " + newWeapon;
    }

    /**
     * Returns a descriptive String
     * @param actor The actor performing the action.
     * @return the text we put on the menu.
     */
    @Override
    public String menuDescription(Actor actor){
        return actor + " crafts a weapon";
    }

}
