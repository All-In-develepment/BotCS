using System.Text;
using System.Runtime.Serialization.Json;
namespace Application.Helpers
{
    public class JsonHelper
    {
        public static string GetJSONString(string url, string coockie)
        {
            using (HttpClient client = new HttpClient())
            {
                client.DefaultRequestHeaders.Add("Cookie", coockie);
                HttpResponseMessage response = client.GetAsync(url).Result;
                response.EnsureSuccessStatusCode();
                string responseBody = response.Content.ReadAsStringAsync().Result;
                // Console.WriteLine(responseBody);
                return responseBody;
            }
        }

        public static T GetObjectFromJSONString<T>(
            string json) where T : new()
        {
            using (MemoryStream stream = new MemoryStream(
                Encoding.UTF8.GetBytes(json)))
            {
                DataContractJsonSerializer serializer =
                    new DataContractJsonSerializer(typeof(T));
                return (T)serializer.ReadObject(stream);
            }
        }

        public static T[] GetArrayFromJSONString<T>(
            string json) where T: new()
        {
            using (MemoryStream stream = new MemoryStream(
                Encoding.UTF8.GetBytes(json)))
            {
                DataContractJsonSerializer serializer =
                    new DataContractJsonSerializer(typeof(T[]));
                return (T[])serializer.ReadObject(stream);
            }
        }
    }
}