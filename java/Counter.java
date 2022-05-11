/*Kata:
Consider an array/list of sheep where some sheep may be missing from
their place. We need a function that counts the number of sheep
present in the array (true means present).
Hint: Don't forget to check for bad values like null/undefined
*/
public class Counter {
	private int numberOfSheep = 0;
	public int countSheeps(Boolean[] arrayOfSheeps) {
		for (int i = 0;i < arrayOfSheeps.length;i++){
			if( Boolean.parseBoolean(String.valueOf(arrayOfSheeps[i])) ){
				numberOfSheep ++;
			}
		}
	return numberOfSheep;
	}
  }