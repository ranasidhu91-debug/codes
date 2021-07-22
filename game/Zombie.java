package game;

import java.util.List;
import java.util.Random;

import edu.monash.fit2099.engine.*;

/**
 * A Zombie 2. Electric Boogaloo
 * Zombie now has a bit of a personality
 *
 *
 * @author Seth
 *
 */
public class Zombie extends ZombieActor {
	/**
	 * List of possible Zombie behaviours
	 */
	private Behaviour[] behaviours = {
			new AttackBehaviour(ZombieCapability.ALIVE),
			new HuntBehaviour(Human.class, 10),
			new WanderBehaviour()
	};
	/**
	 * probability of biting
	 */
	private double probOfBite;
	/**
	 * How many movement actions per turn
	 */
	private double speed;
	/**
	 * Can it use a move action this turn?
	 */
	private boolean canMove;
	/**
	 * counter to keep track of behaviours
	 */
	private int counter = 0;
	/**
	 * Used across Zombie for chance based interactions such as biting
	 */
	private Random rand = new Random();


	/**
	 * Zombie Constructor
	 * sets zombie variables
	 * @param name Name of the Zombie
	 */
	public Zombie(String name) {
		super(name, 'Z', 100, ZombieCapability.UNDEAD);
		for (int i = 0; i <2; i++){
			addItemToInventory(new ZombieArm());
			addItemToInventory(new ZombieLeg());
		}
		this.probOfBite = calcProbOfBite();
		this.speed = calcSpeed();
		this.canMove = true;
	}

	/**
	 * Probability of either setting the IntrinsicWeapon as a bite or punch, based on bite
	 * probability which is based on number of arms
	 * @return a new IntrinsicWeapon that is either a bite or a punch
	 */
	@Override
	public IntrinsicWeapon getIntrinsicWeapon() {
		this.probOfBite = calcProbOfBite();
		if (rand.nextDouble()<probOfBite){
			return new IntrinsicWeapon(12, "bites");
		} else {
			return new IntrinsicWeapon(10, "punches");
		}
	}

	/**
	 * If a Zombie can attack, it will.  If not, it will chase any human within 10 spaces.
	 * If no humans are close enough it will wander randomly.
	 * Zombies can lose legs, which will affect how often they can execute a move function such as wander or hunt
	 * if both legs are gone, then zombie can do either.
	 *
	 * @param actions list of possible Actions
	 * @param lastAction previous Action, if it was a multiturn action
	 * @param map the map where the current Zombie is
	 * @param display the Display where the Zombie's utterances will be displayed
	 */
	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		int counter = 0;
		for (Behaviour behaviour : behaviours) {
			if (counter == 1 || counter == 2) {
				if (this.calcSpeed()<0.6) {
					if (rand.nextBoolean()) {
						Action action = behaviour.getAction(this, map);
						if (action != null)
							return action;
					}
				}
				else{
					Action action = behaviour.getAction(this, map);
					if (action != null)
						return action;
				}
			}
			else{
				Action action = behaviour.getAction(this, map);
				if (action != null)
					return action;
			}
			counter ++;
		}
//		if (rand.nextDouble()<0.1){
//			Action brains = new Action();
//		}
		return new DoNothingAction();
	}

	/**
	 * Calculate the probability of the zombie to bite
	 * @return the probability as a double.
	 */
	private double calcProbOfBite(){
		if (this.getNumberOfArms() == 2){
			return .5;
		}else if (this.getNumberOfArms() == 1){
			return .75;
		}else {
			return 1;
		}
	}

	/**
	 * Calculate the zombie's speed
	 * @return the speed as a double
	 */
	private double calcSpeed(){
		if (this.getNumberOfLegs() == 2){
			return 1.0;
		}else if (this.getNumberOfLegs() == 1){
			return .5;
		}else {
			return 0;
		}
	}

	/**
	 * Counts the number of Zombie Arms in the Zombie's inventory
	 * @return int Number of arms
	 */
	private int getNumberOfArms(){
		int numArm = 0;
		List<Item> inventory = this.getInventory();
		for(Item item:inventory){
			if (item.toString().equals("Zombie Arm")){
				numArm ++;
			}
		}
		return numArm;
	}
	/**
	 * Counts the number of Zombie Legs in the Zombie's inventory
	 * @return int Number of legs
	 */
	private int getNumberOfLegs(){
		int numLeg = 0;
		List<Item> inventory = this.getInventory();
		for(Item item:inventory){
			if (item.toString().equals("Zombie Leg")){
				numLeg ++;
			}
		}
		return numLeg;
	}

}
