package game;

import edu.monash.fit2099.engine.*;
import java.util.Random;
import java.util.Arrays;
import java.util.Collections;

/**
 * Class representing an ordinary human.
 * 
 * 
 * @author ram
 *
 */
public class Human extends ZombieActor {
	/**
	 * A list of possible behaviours by the Human.
	 */
	private Behaviour [] behaviours = {
			new WanderBehaviour(),
			new EatBehaviour(ZombieCapability.FOOD),
			new PickDropBehaviour(ZombieCapability.FOOD),
			new CraftBehaviour(ZombieCapability.CRAFT)
	};


	/**
	 * The default constructor creates default Humans. Adds the capability ZombieCapability.FOOD
	 * 
	 * @param name the human's display name
	 */
	public Human(String name) {
		super(name, 'H', 50, ZombieCapability.ALIVE);
		addCapability(ZombieCapability.FOOD);
	}
	
	/**
	 * The protected constructor can be used to create subtypes
	 * of Human, such as the Player
	 * 
	 * @param name the human's display name
	 * @param displayChar character that will represent the Human in the map 
	 * @param hitPoints amount of damage that the Human can take before it dies
	 */
	protected Human(String name, char displayChar, int hitPoints) {
		super(name, displayChar, hitPoints, ZombieCapability.ALIVE);

	}

	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		// FIXME humans are pretty dumb, maybe they should at least run away from zombies?
		//return behaviour.getAction(this,map);
		Collections.shuffle(Arrays.asList(behaviours));
		for (Behaviour behaviour : behaviours){
			Action action = behaviour.getAction(this,map);
			if(action != null){
				return action;
			}
		}
		return new DoNothingAction();
	}

}
