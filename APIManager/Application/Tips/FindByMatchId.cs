using Application.Core;
using AutoMapper;
using AutoMapper.QueryableExtensions;
using MediatR;
using Microsoft.EntityFrameworkCore;
using Persistence;

namespace Application.Tips
{
    public class FindByMatchId
    {
        public class Query : IRequest<Result<TipDto>>
        {
            public string MatchId { get; set; }
        }

        public class Handler : IRequestHandler<Query, Result<TipDto>>
        {
            private readonly DataContext _context;
            private readonly IMapper _mapper;

            public Handler(DataContext context, IMapper mapper)
            {
                _mapper = mapper;
                _context = context;
            }

            public async Task<Result<TipDto>> Handle(Query request, CancellationToken cancellationToken)
            {
                var tip = await _context.Tips
                    .ProjectTo<TipDto>(_mapper.ConfigurationProvider)
                    .FirstOrDefaultAsync(x => x.TipMatchId == request.MatchId);

                return Result<TipDto>.Success(tip);
            }
        }
    }
}