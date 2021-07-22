package game;

import edu.monash.fit2099.engine.WeaponItem;


/**
 * The arms of the forbidden one.
 * Its literally just the arm(s) of a zombie, and it goes bonk.
 * Also adds the zombie Capability CRAFTABLE, which will allow the item to be crafted
 * @author Seth
 *
 */
public class ZombieArm extends WeaponItem {
    public ZombieArm(){
        super("Zombie Arm",'i',3,"bonk");
        this.addCapability(ZombieCapability.CRAFTABLE);
    }

}
