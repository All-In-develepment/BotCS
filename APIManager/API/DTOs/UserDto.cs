namespace API.DTOs
{
    public class UserDto
    {
        public string DisplayName { get; set; }
        public string Token { get; set; }
        public string Image { get; set; }
        public string Username { get; set; }
        public DateTime JoinDate { get; set; }
        public DateTime ExpireDate { get; set; }
    }
}