import java.security.*;
import java.util.Arrays;
import java.util.Base64;
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
 
public class aes {
 
    private static SecretKeySpec secretKey;

   public static String encrypt(String strToEncrypt, String secret) 
    {
        try
        {
            secretKey = new SecretKeySpec(secret.getBytes("UTF-8"), "AES");
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes("UTF-8")));
        } 
        catch (Exception e) 
        {
            System.out.println("Error while encrypting: " + e.toString());
        }
        return null;
    }
 
    public static String decrypt(String strToDecrypt, String secret) 
    {
        try
        {
            
            secretKey = new SecretKeySpec(secret.getBytes("UTF-8"), "AES");
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
        } 
        catch (Exception e) 
        {
            System.out.println("Error while decrypting: " + e.toString());
        }
        return null;
    }
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter plaintext:\n");
        String pt=sc.nextLine();
        System.out.println("enter key of exactly 16 bytes:\n");
//error if key<16 or key>16
        String k=sc.nextLine();
        String cipher=encrypt(pt,k);
        System.out.println("encrypted text is:\n"+cipher);
        String plain=decrypt(cipher,k);
        System.out.println("decrypted text is:\n"+plain);
        
    }
    
}
