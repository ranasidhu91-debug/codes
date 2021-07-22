package game;

import java.util.Random;

import edu.monash.fit2099.engine.*;

/**
 * Special Action for attacking other Actors.
 */
public class AttackAction extends Action {

	/**
	 * The Actor that is to be attacked
	 */
	protected Actor target;
	/**
	 * Random number generator
	 */
	protected Random rand = new Random();

	/**
	 * Constructor.
	 * 
	 * @param target the Actor to attack
	 */
	public AttackAction(Actor target) {
		this.target = target;
	}

	/**
	 * Performs the action. If the actor that is not conscious is a Human, then the corpse would become a Zombie that
	 * that would also have the ZombieCapability.RISE. Both Zombie and Mambo Marie have the ZombieCapability UNDEAD and ARISE.
	 * So while both of them would die at the end, Mambo Marie would change the boolean value of HailItem.Alive t0 false
	 * to prevent HailItem from calling Mambo Marie again.
	 * @param actor The actor performing the action.
	 * @param map The map the actor is on.
	 * @return a description of what happened that can be displayed to the user
	 */
	@Override
	public String execute(Actor actor, GameMap map) {

		Weapon weapon = actor.getWeapon();

		if (rand.nextBoolean()) {
			return actor + " misses " + target + ".";
		}

		int damage = weapon.damage();
		String result = actor + " " + weapon.verb() + " " + target + " for " + damage + " damage.";

		if (weapon.verb().equals("bites")){
			target.heal(5);
			result += target + " heals for " + 5 + "hp";
		}


		target.hurt(damage);
		if (!target.isConscious()) {
			if(target.hasCapability(ZombieCapability.ALIVE)){
				target.removeCapability(ZombieCapability.ALIVE);
				Corpse corpse = new Corpse("dead " + target, '%');
				corpse.addCapability(ZombieCapability.RISE);
				map.locationOf(target).addItem(corpse);

				Actions dropActions = new Actions();
				for (Item item : target.getInventory())
					dropActions.add(item.getDropAction());
				for (Action drop : dropActions)
					drop.execute(target, map);
				map.removeActor(target);

				result += System.lineSeparator() + target + " is killed.";
			}
			if(target.hasCapability(ZombieCapability.UNDEAD)){
				target.removeCapability(ZombieCapability.UNDEAD);
				Actions dropActions = new Actions();
				for(Item item : target.getInventory())
					if (!item.toString().equals("punches") && rand.nextDouble()<0.25) {
						dropActions.add(item.getDropAction());
					}
				for (Action drop: dropActions)
					drop.execute(target,map);
				if(target.hasCapability(ZombieCapability.ARISE)){
					HailItem.alive = false;
				}
				map.removeActor(target);

				result += System.lineSeparator() + target + " is killed and disintegrates.";
			}
		}
		else if (target.isConscious()){
			if(target.hasCapability(ZombieCapability.UNDEAD)){
				if (rand.nextDouble()<0.2){
					Actions loseLimb = new Actions();
					if (rand.nextBoolean()){
						for(Item item : target.getInventory()){
							if (item.toString().equals("Zombie Leg")){
								loseLimb.add(item.getDropAction());
								target.removeItemFromInventory(item);
							}
						}
					}
					else{
						for(Item item : target.getInventory()){
							if (item.toString().equals("Zombie Arm")){
								loseLimb.add(item.getDropAction());
								target.removeItemFromInventory(item);
							}
						}
					}
					for (Action drop: loseLimb)
						drop.execute(target,map);
				}
			}
		}
		return result;
	}

	/**
	 * Returns a descriptive String
	 * @param actor The actor performing the action.
	 * @return the text we put on the menu
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " attacks " + target;
	}
}
