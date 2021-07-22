package game;

import java.util.Arrays;
import java.util.List;

import edu.monash.fit2099.engine.*;

/**
 * The main class for the zombie apocalypse game.
 *
 */
public class Application {

	public static void main(String[] args) {
		World world = new World(new Display());

		FancyGroundFactory groundFactory = new FancyGroundFactory(new Dirt(), new Fence(), new Tree());

		
		List<String> map = Arrays.asList(
		"................................................................................",
		"................................................................................",
		"....................................##########..................................",
		"..........................###########........#####..............................",
		"............++...........##......................########.......................",
		"..............++++.......#..............................##......................",
		".............+++...+++...#...............................#......................",
		".........................##..............................##.....................",
		"..........................#...............................#.....................",
		".........................##...............................##....................",
		".........................#...............................##.....................",
		".........................###..............................##....................",
		"...........................####......................######.....................",
		"..............................#########.........####............................",
		"............+++.......................#.........#...............................",
		".............+++++....................#.........#...............................",
		"...............++........................................+++++..................",
		".............+++....................................++++++++....................",
		"............+++.......................................+++.......................",
		"................................................................................",
		".........................................................................++.....",
		"........................................................................++.++...",
		".........................................................................++++...",
		"..........................................................................++....",
		"................................................................................");
		List<String> town = Arrays.asList(
				"......................................................................",
				"......................................................................",
				"..........................##########..................................",
				"...................................#####..............................",
				"..++...................................########.......................",
				"....++++..............................................................",
				"...+++...+++..........................................................",
				"...#..................................................................",
				"...#.....................#######......................................",
				"...#..................................................................",
				"...#..................................................................",
				"...............###....................................................",
				".................####......................######.....................",
				"......................................................................");

		GameMap gameMap = new GameMap(groundFactory, map );
		GameMap townMap = new GameMap(groundFactory,town);
		world.addGameMap(gameMap);
		world.addGameMap(townMap);

		Vehicle jeep = new Vehicle();
		jeep.addAction(new MoveActorAction(townMap.at(20,13),"to town"));
		gameMap.at(45,15).addItem(jeep);

		Vehicle jeep2 = new Vehicle();
		jeep2.addAction(new MoveActorAction(gameMap.at(45,15),"to farm"));
		townMap.at(20,13).addItem(jeep2);

		Actor player = new Player("Player", '@', 100);
		world.addPlayer(player, gameMap.at(42, 17));


		gameMap.at(74,21).addItem(new HailItem("Hail"));

//	     Place some random humans
		String[] humans = {"Carlton", "May", "Vicente", "Andrea", "Wendy",
				"Elina", "Winter", "Clem", "Jacob", "Jaquelyn"};
		int x, y;
		for (String name : humans) {
			do {
				x = (int) Math.floor(Math.random() * 20.0 + 30.0);
				y = (int) Math.floor(Math.random() * 7.0 + 5.0);
			}
			while (gameMap.at(x, y).containsAnActor());
			gameMap.at(x,  y).addActor(new Human(name));
		}

		String[] farmers = {"Rana","Meninder"};
		int a,b;
		for(String name : farmers){
			do{
				a = (int) Math.floor(Math.random() * 20.0 + 40.0);
				b = (int) Math.floor(Math.random() * 9.0 + 6.0);
			}
			while (gameMap.at(a,b).containsAnActor());
			gameMap.at(a,b).addActor(new Farmer(name));
		}

		// place a simple weapon
		gameMap.at(45, 12).addItem(new Plank());


		// FIXME: Add more zombies!
		gameMap.at(50, 15).addActor(new Zombie("Groan"));
		gameMap.at(30,  18).addActor(new Zombie("Boo"));
		gameMap.at(10,  4).addActor(new Zombie("Uuuurgh"));
		gameMap.at(50, 18).addActor(new Zombie("Mortalis"));
		gameMap.at(11, 10).addActor(new Zombie("Gaaaah"));
		gameMap.at(58, 14).addActor(new Zombie("Aaargh"));
		gameMap.at(35,18).addActor(new Zombie("Berghhhhh"));

		townMap.at(30,9).addActor(new Zombie("Dia"));
		townMap.at(50,2).addActor(new Zombie("Kerna"));
		townMap.at(12,8).addActor(new Zombie("Psdsd"));
		townMap.at(7,4).addActor(new Zombie("Sharon"));
		townMap.at(17,7).addActor(new Zombie("Natasha"));
		townMap.at(13,5).addActor(new Zombie("Hema"));
		townMap.at(40,8).addActor(new Zombie("Ghajini"));

		townMap.at(30,7).addActor(new Human("Christine"));
		townMap.at(33,13).addActor(new Human("Dinish"));
		townMap.at(25,10).addActor(new Human("Angellica"));
		townMap.at(29,9).addActor(new Human("Janak"));
		townMap.at(45,5).addActor(new Farmer("Rafiq"));
		townMap.at(28,6).addActor(new Farmer("Amalyna"));
		world.run();
	}
}
