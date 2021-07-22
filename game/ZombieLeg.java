package game;

import edu.monash.fit2099.engine.WeaponItem;

/**
 * The legs of the forbidden one.
 * Its literally just the leg(s) of a zombie, and it goes thwack.
 * Also adds the zombie Capability CRAFTABLE, which will allow the item to be crafted
 * @author Seth
 *
 */
public class ZombieLeg extends WeaponItem {
    public ZombieLeg(){
        super("Zombie Leg",'l',4,"thwack");
        this.addCapability(ZombieCapability.CRAFTABLE);
    }

}
