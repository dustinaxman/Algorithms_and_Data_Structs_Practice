import java.util.*;
public class HellowWorld {
	public static void main(String[] args) {
		HashMap<String,Double> hm = new HashMap<String,Double>();
		hm.put("Dustin",10.5);
		System.out.println(hm);
		double[][] a={{2,3},{1,2}};
		System.out.println(a[0][0]);
		System.out.println(a[0][1]);
		System.out.println(a[1][0]);
		System.out.println(a[1][1]);
		double[][] b={{2,3},{1,2}};
		double[][] c=new double[2][2];
		for(int i=0;i<2;i++){
			for(int i3=0;i3<2;i3++){
				double tmpSum=0;
				for(int i2=0;i2<2;i2++){
					System.out.println("A:"+Double.toString((a[i][i2]))+" B:"+Double.toString((b[i2][i3])));
					tmpSum=tmpSum+a[i][i2]*b[i2][i3];
				}
				c[i][i3]=tmpSum;
			
			}
		    
		}
		System.out.println(c[0][0]);
		System.out.println(c[0][1]);
		System.out.println(c[1][0]);
		System.out.println(c[1][1]);

	}

}
